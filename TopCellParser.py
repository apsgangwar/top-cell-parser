# Give the verilog file path and the name module to count instances
verilog_file_path = "/Users/apsgangwar/demo/TopCell.v"
module_to_count_instances = "TopCell"


def verilogFileParser(file_path):
    file = open(file_path, "r")

    parsed_modules = {}  # contains all the parsed modules and its data

    module_name = ""
    output_declarations = []
    input_declarations = []
    wire_declarations = []
    instance_declarations = {}

    for line in file.readlines():
        # Checking for comments in line and filtering them
        comment_index = line.find("//")
        line = line[0:comment_index]
        line = line.strip()
        if line == "":
            continue

        # Splitting the line into separate words
        commands = line.replace(';', '').split()
        check_command = commands[0]

        if check_command == "module":
            module_name = commands[1]

        elif check_command == "output":
            output_declarations.append(commands[1:])

        elif check_command == "input":
            input_declarations.append(commands[1:])

        elif check_command == "wire":
            wire_declarations.append(commands[1:])

        elif check_command == "endmodule":
            # Setting the declarations wrt modules
            parsed_modules[module_name] = {
                "output_declarations": output_declarations,
                "input_declarations": input_declarations,
                "wire_declarations": wire_declarations,
                "instance_declarations": instance_declarations,
            }

            # Reinitialising the variables
            module_name = ""
            output_declarations = []
            input_declarations = []
            wire_declarations = []
            instance_declarations = {}

        else:
            if check_command in instance_declarations:
                instance_declarations[check_command].append(
                    {
                        "instance_name": commands[1],
                        "instance_params": " ".join(commands[2:]),
                    }
                )
            else:
                instance_declarations[check_command] = [
                    {
                        "instance_name": commands[1],
                        "instance_params": " ".join(commands[2:]),
                    }
                ]

    file.close()
    return parsed_modules


def countInstances(parsed_modules, module_to_check, recursive_flag=False):
    if module_to_check in parsed_modules:
        count = {}
        if recursive_flag:  # include itself also if sub_module
            count[module_to_check] = 1

        instance_declarations = parsed_modules[module_to_check]["instance_declarations"]
        for sub_module in instance_declarations:
            sub_module_placements = len(instance_declarations[sub_module])
            sub_module_instances = countInstances(parsed_modules, sub_module, True)

            for instance in sub_module_instances:
                if instance in count:
                    count[instance] += (
                        sub_module_placements * sub_module_instances[instance]
                    )
                else:
                    count[instance] = (
                        sub_module_placements * sub_module_instances[instance]
                    )

        return count

    else:
        return {module_to_check: 1}


def printInstanceCount(count):
    row_format = "{:<12}  :  {} placements"
    for instance in count:
        print(row_format.format(instance, count[instance]))


parsed_modules = verilogFileParser(verilog_file_path)
instance_count = countInstances(parsed_modules, module_to_count_instances)
printInstanceCount(instance_count)
