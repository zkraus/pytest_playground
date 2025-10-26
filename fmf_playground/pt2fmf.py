from loguru import logger
import os
import subprocess
import fmf
import yaml


def get_pytest_test_cases() -> list[str]:
    pytest_test_cases = [
        x
        for x in subprocess.run(["pytest", "--co", "-q"], capture_output=True)
        .stdout.decode("utf-8")
        .splitlines()[:-2]
    ]
    return pytest_test_cases


def get_fmf_tree() -> fmf.Tree:
    fmf_tree = fmf.Tree(".")
    return fmf_tree


def filter_existing_test_cases(
    tree: fmf.Tree, test_cases: list[tuple[str, str]]
) -> list[tuple[str, str]]:

    non_existing_test_cases = [
        x for x in test_cases if not tree.find(f"/{x[0]}/::{x[1]}")
    ]
    return non_existing_test_cases


def split_test_case_name(test_case_name: str) -> tuple[str, str]:
    test_path, test_name = test_case_name.split("::", maxsplit=1)
    return test_path, test_name


def fmfmize_test_path(test_path):
    file_pathname = os.path.join(os.getcwd(), f"{test_path}.fmf")
    return file_pathname


def fmfmize_test_name(test_name):
    return f"/::{test_name}"


def fmf_file_exists_or_create(test_path: str) -> bool:
    file_pathname = fmfmize_test_path(test_path)
    file_path = os.path.dirname(file_pathname)
    if not os.path.exists(file_path):
        logger.info(f"Creating {file_pathname}")
        os.makedirs(file_path)
    if not os.path.exists(file_pathname):
        with open(file_pathname, "w") as f:
            logger.info(f"Writing {file_pathname}")
            f.write("")


def append_non_existing_test_case(test_path, test_name):
    fmf_file_exists_or_create(test_path)
    test_pathname = fmfmize_test_path(test_path)
    fmf_test_name = fmfmize_test_name(test_name)
    with open(test_pathname, "a") as f:
        logger.info(f"Appending {fmf_test_name} into {test_pathname}")

        tc_object = {fmf_test_name: {"TODO": "define metadata"}}

        yaml_dump_test_name = yaml.dump(tc_object)
        f.write(yaml_dump_test_name)
        f.write("\n")


if __name__ == "__main__":
    tree = get_fmf_tree()
    pytest_test_cases = get_pytest_test_cases()
    split_test_cases = [split_test_case_name(x) for x in pytest_test_cases]
    non_existing_test_cases = filter_existing_test_cases(tree, split_test_cases)
    logger.debug(non_existing_test_cases)

    for test_case in non_existing_test_cases:
        test_path, test_name = test_case
        append_non_existing_test_case(test_path, test_name)

    # print(non_existing_test_cases)
