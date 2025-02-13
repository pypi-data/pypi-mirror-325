"""Tests for the ASE interface."""

import pytest

from pyfhiaims import AimsStdout


def test_ase_interface_outputs(data_dir):

    try:
        from pyfhiaims.external_interfaces.ase.io import read_aims_results
    except ImportError:
        pytest.skip("No ASE installed.")

    output_file = data_dir / "stdout" / "relax.out.gz"
    ase_results = read_aims_results(output_file, verbosity="all")
    from pprint import pprint
    pprint(ase_results)


def test_docs_control_in(data_dir):
    from pyfhiaims.outputs.parser import StdoutParser, converters
    from pyfhiaims.outputs.parser.abc import FLOAT
    output_file = data_dir / "stdout" / "output_files" / "QMMM.out"
    parser = StdoutParser(output_file)
    parser.add_parsed_values("scf_step",
                             occ_numbers=converters.to_vector(
                                 rf"  \| Occupation number: *({FLOAT})",
                                    dtype=float,
                                    multistring=True))
    stdout = AimsStdout(output_file, parser)
    print(stdout.results["ionic_steps"][0]["scf_steps"][-1]["occ_numbers"])
