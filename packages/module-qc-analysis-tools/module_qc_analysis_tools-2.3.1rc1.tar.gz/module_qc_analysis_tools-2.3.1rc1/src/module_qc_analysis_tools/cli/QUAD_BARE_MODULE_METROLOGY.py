from __future__ import annotations

import json
import logging
from datetime import datetime
from pathlib import Path

import typer
from module_qc_data_tools import (
    load_json,
    outputDataFrame,
    qcDataFrame,
    save_dict_list,
)

from module_qc_analysis_tools import __version__
from module_qc_analysis_tools.cli.globals import (
    CONTEXT_SETTINGS,
    OPTIONS,
    LogLevel,
)
from module_qc_analysis_tools.utils.misc import (
    get_inputs,
)

app = typer.Typer(context_settings=CONTEXT_SETTINGS)


@app.command()
def main(
    input_meas: Path = OPTIONS["input_meas"],
    base_output_dir: Path = OPTIONS["output_dir"],
    # qc_criteria_path: Path = OPTIONS["qc_criteria"],
    # layer: str = OPTIONS["layer"],
    verbosity: LogLevel = OPTIONS["verbosity"],
):
    log = logging.getLogger(__name__)
    log.setLevel(verbosity.value)

    log.info("")
    log.info(" ===================================================")
    log.info(" \tPerforming QUAD_BARE_MODULE_METROLOGY analysis")
    log.info(" ===================================================")
    log.info("")

    test_type = Path(__file__).stem

    time_start = round(datetime.timestamp(datetime.now()))
    output_dir = base_output_dir.joinpath(test_type).joinpath(f"{time_start}")
    output_dir.mkdir(parents=True, exist_ok=False)

    allinputs = get_inputs(input_meas)
    # qc_config = get_qc_config(qc_criteria_path, test_type)

    # alloutput = []
    # timestamps = []
    for filename in sorted(allinputs):
        log.info("")
        log.info(f" Loading {filename}")
        # meas_timestamp = get_time_stamp(filename)

        inputDFs = load_json(filename)
        log.info(
            f" There are results from {len(inputDFs)} module(s) stored in this file"
        )

        with Path(filename).open(encoding="utf-8") as f:
            jsonData = json.load(f)

        for j, inputDF in zip(jsonData, inputDFs):
            d = inputDF.to_dict()

            results = j[0].get("results")
            props = results.get("property")
            metadata = results.get("metadata")
            if metadata is None:
                metadata = results.get("Metadata")

            module_name = d.get("serialNumber")
            meas = results.get("Measurements")
            # alternatively, props.get("MODULE_SN")

            #  input data

            if "SENSOR_X" in meas:
                results["SENSOR_X"] = round(meas["SENSOR_X"], 3)

            if "SENSOR_Y" in meas:
                results["SENSOR_Y"] = round(meas["SENSOR_Y"], 3)

            if "FECHIPS_X" in meas:
                results["FECHIPS_X"] = round(meas["FECHIPS_X"], 3)

            if "FECHIPS_Y" in meas:
                results["FECHIPS_Y"] = round(meas["FECHIPS_Y"], 3)

            if "FECHIP_THICKNESS" in meas:
                results["FECHIP_THICKNESS"] = round(meas["FECHIP_THICKNESS"], 3)

            if "FECHIP_THICKNESS_STD_DEVIATION" in meas:
                results["FECHIP_THICKNESS_STD_DEVIATION"] = round(
                    meas["FECHIP_THICKNESS_STD_DEVIATION"], 3
                )

            if "BARE_MODULE_THICKNESS" in meas:
                results["BARE_MODULE_THICKNESS"] = round(
                    meas["BARE_MODULE_THICKNESS"], 3
                )

            if "BARE_MODULE_THICKNESS_STD_DEVIATION" in meas:
                results["BARE_MODULE_THICKNESS_STD_DEVIATION"] = round(
                    meas["BARE_MODULE_THICKNESS_STD_DEVIATION"], 3
                )

            if "SENSOR_THICKNESS" in meas:
                results["SENSOR_THICKNESS"] = round(meas["SENSOR_THICKNESS"], 3)

            if "SENSOR_THICKNESS_STD_DEVIATION" in meas:
                results["SENSOR_THICKNESS_STD_DEVIATION"] = round(
                    meas["SENSOR_THICKNESS_STD_DEVIATION"], 3
                )

            def withinTolerance(x, x0, dxplus, dxminus):
                # if x >= (x0 - abs(dxminus)) and x <= (x0 + dxplus):
                #    return True
                # else:
                #    return False
                return (x0 - abs(dxminus)) <= x <= (x0 + dxplus)

            #  Simplistic QC criteria
            a = 0
            if not withinTolerance(results["SENSOR_X"], 39.5, 0.05, 0.0):
                a += 1
            if not withinTolerance(results["SENSOR_Y"], 41.1, 0.05, 0.0):
                a += 1

            if not withinTolerance(results["FECHIPS_X"], 42.187, 0.07, 0.0):
                a += 1
            if not withinTolerance(results["FECHIPS_Y"], 40.255, 0.07, 0.0):
                a += 1

            if not withinTolerance(results["FECHIP_THICKNESS"], 150.0, 25.0, -10.0):
                a += 1
            if not withinTolerance(
                results["FECHIP_THICKNESS_STD_DEVIATION"], 50.0, 50.0, 50.0
            ):
                a += 1

            if not withinTolerance(
                results["BARE_MODULE_THICKNESS"], 325.0, 50.0, -50.0
            ):
                a += 1
            if not withinTolerance(
                results["BARE_MODULE_THICKNESS_STD_DEVIATION"], 50.0, 50.0, 50.0
            ):
                a += 1

            if not withinTolerance(results["SENSOR_THICKNESS"], 150.0, 50.0, -15.0):
                a += 1
            if not withinTolerance(
                results["SENSOR_THICKNESS_STD_DEVIATION"], 50.0, 50.0, 50.0
            ):
                a += 1

            passes_qc = a == 0

            #  Output a json file
            outputDF = outputDataFrame()
            outputDF.set_test_type(test_type)
            data = qcDataFrame()

            if metadata is not None:
                data._meta_data.update(metadata)

            #  Pass-through properties in input
            for key, value in props.items():
                data.add_property(key, value)

            #  Add analysis version
            data.add_property(
                "ANALYSIS_VERSION",
                __version__,
            )

            #  Pass-through measurement parameters
            for key, value in results.items():
                if key in [
                    "property",
                    "metadata",
                    "Metadata",
                    "Measurements",
                    "comment",
                    "DOMINANT_DEFECT",
                ]:
                    continue

                data.add_parameter(key, value)

            outputDF.set_results(data)
            outputDF.set_pass_flag(passes_qc)

            outfile = output_dir.joinpath(f"{module_name}.json")
            log.info(f" Saving output of analysis to: {outfile}")
            out = outputDF.to_dict(True)
            out.update({"serialNumber": module_name})
            save_dict_list(outfile, [out])


if __name__ == "__main__":
    typer.run(main)
