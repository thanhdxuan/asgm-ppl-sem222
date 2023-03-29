    # + , - , *, / accept their operands in int type and return int type
    # +., -., *., /. accept their operands in float type and return float type
    # > and = accept their operands in int type and return bool type
    # >. and =. accept their operands in float type and return bool type
    # !, &&, ||, >b and =b accept their operands in bool type and return bool type
    # i2f accepts its operand in int type and return float type
    # floor accept its operand in float type and return int type
    # In an Assign, the type of lhs must be the same as that of rhs, otherwise, the exception TypeMismatchInStatement should be raised together with the Assign
    # the type of an Id is inferred from the above constraints in the first usage, 
    #     if the Id is not in the declarations, exception UndeclaredIdentifier should be raised together with the name of the Id, or
    #     If the Id cannot be inferred in the first usage, exception TypeCannotBeInferred should be raised together with the name of the identifier
