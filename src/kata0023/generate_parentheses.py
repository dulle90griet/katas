def gen_confs(target, cols, max_node=None, generated=None):
    if max_node is None:
        max_node = target
        
    if cols == 1:
        return [[target]] if target <= max_node else []

    configs = []

    if cols == 2:
        for i in range(1, max_node):
            complement = target - i
            if 0 < complement <= max_node:
                configs.append([i, complement])
        return configs

    for i in range(1, max_node):
        for config in gen_confs(target - i, cols - 1, target, generated):
            configs.append([i] + config)
    return configs


def gen_parenths(n, max_children=None):    
    if max_children is None:
        max_children = n
        
    if n == 1:
        return ["()"]

    solutions = []
    child_counts = list(range(1, max_children+1))
    for child_count in child_counts:
        configs = gen_confs(n, child_count)
        for config in configs:
            if len(config) == 1:
                node_parenths = gen_parenths(config[0] - 1)
                solutions += ["(" + node_parenth + ")" for node_parenth in node_parenths]
            else:
                config_parenths = []
                for node_value in config:
                    node_parenths = gen_parenths(node_value, 1)
                    if not config_parenths:
                        config_parenths = node_parenths
                    else:
                        config_parenths = [prev_parenths + node_parenth for node_parenth in node_parenths
                                            for prev_parenths in config_parenths]
                solutions += config_parenths

    return solutions
