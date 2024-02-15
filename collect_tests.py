#!/usr/bin/python3

import os, json

all_tests = []
defs = {}


def get_tests(dir):
    files = []
    for item in os.listdir(dir):
        path = os.path.join(dir, item).replace("\\", "/")
        if os.path.isdir(path):
            files = [*files, *get_tests(path)]
        else:
            files.append(path)
    return files


def get_defs_names(file):
    content = open(file, "r").read()
    defs = []
    for line in content.split("\n"):
        if "def test_" in line:
            defs.append(line.split("(")[0].replace("def test_", "").replace(" ", ""))
    return defs


all_tests = get_tests("./tests")

for file in all_tests:
    defs[file] = get_defs_names(file)

print(json.dumps(defs, indent=2))

{
    "./tests/test_console.py": [
        "help",
        "help_EOF",
        "help_all",
        "help_count",
        "help_quit",
        "help_update",
        "do_create",
        "show",
        "show_error",
        "destroy",
        "destroy_error",
        "update",
        "update_error",
        "all_class",
        "destroy_valid",
        "destroy_invalid_class",
        "destroy_invalid_id",
        "update_valid",
        "update_invalid_class",
        "help",
        "create",
        "show",
        "destroy",
        "all",
        "update",
        "quit",
        "EOF",
        "emptyline",
        "basedotall",
        "reviewdotall",
        "userdotall",
        "statedotall",
        "placedotall",
        "amenitydotall",
        "citydotall",
        "basedotcount",
        "userdotcount",
        "statedotcount",
        "placedotcount",
        "citydotcount",
        "amenitydotcount",
        "reviewdotcount",
        "basedotshow",
        "userdotshow",
        "citydotshow",
        "statedotshow",
        "placedotshow",
        "amenitydotshow",
        "reviewdotshow",
        "reviewdotdestroy",
        "basedotdestroy",
        "userdotdestroy",
        "placedotdestroy",
        "statedotdestroy",
        "citydotdestroy",
        "amenitydotdestroy",
        "basedotupdate",
        "userdotupdate",
        "placedotupdate",
        "statedotupdate",
        "citydotupdate",
        "amenitydotupdate",
        "reviewdotupdate",
    ],
    "./tests/test_models/test_amenity.py": [
        "amenity_is_a_subclass_of_basemodel",
        "attr_is_a_class_attr",
        "class_attr",
    ],
    "./tests/test_models/test_base_model.py": [
        "class_type",
        "class_docstring",
        "module_docstrings",
        "init",
        "adding_attributes",
        "str",
        "save",
        "to_dict",
        "to_dict_values",
        "recreate_instance",
        "string_input",
        "from_dict",
        "json",
        "all",
        "kwargs",
        "undefined_input",
        "inf_input",
        "nan_input",
        "string_kwargs",
        "unknown_kwargs",
        "int_kwargs",
        "float_kwargs",
        "inf_kwargs",
        "nan_kwargs",
        "empty_dict",
        "undefined_dict",
        "string_dict",
        "int_dict",
        "float_dict",
        "inf_dict",
        "nan_dict",
        "None",
        "manual_kwargs",
        "manual_kwargs_none",
        "manual_kwargs_int",
        "manual_kwargs_float",
        "manual_kwargs_inf",
        "manual_kwargs_nan",
        "manual_kwargs_unknown",
    ],
    "./tests/test_models/test_city.py": [
        "city_is_a_subclass_of_basemodel",
        "attrs_are_class_attrs",
    ],
    "./tests/test_models/test_engine/test_file_storage.py": [
        "file_path_is_a_private_class_attr",
        "objects_is_a_private_class_attr",
        "init_without_arg",
        "init_with_arg",
        "storage_initialization",
        "all_method",
        "new_method",
        "save_method",
        "reload_method",
    ],
    "./tests/test_models/test_engine/__init__.py": [],
    "./tests/test_models/test_place.py": [
        "attrs_are_class_attrs",
        "class_attrs",
        "place_obj_is_a_subclass_of_basemodel",
    ],
    "./tests/test_models/test_review.py": [
        "review_is_a_subclass_of_basemodel",
        "attrs_are_class_attrs",
        "class_attrs",
    ],
    "./tests/test_models/test_state.py": [
        "state_is_a_subclass_of_basemodel",
        "attr_is_a_class_attr",
        "class_attrs",
    ],
    "./tests/test_models/test_user.py": [
        "user_instance",
        "user_attributes",
        "user_attribute_types",
        "user_inherited_attributes",
        "user_str_representation",
        "user_to_dict_method",
        "user_save_method",
    ],
    "./tests/test_models/__init__.py": [],
    "./tests/__init__.py": [],
}
