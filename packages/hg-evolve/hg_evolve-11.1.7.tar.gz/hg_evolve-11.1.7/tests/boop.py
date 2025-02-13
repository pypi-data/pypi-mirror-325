def boop(repo, node, predecessors):
    # XXX we might need a tree of markers :(
    #       3
    #        \
    # 0 - 1 - 2 - 5 - 6
    #        /
    #       4
    # 6 was rewritten from 0 using amend (and fold)???

    """

    >>> list(boop({0, 6}, 6, {
    ...     1: [(0, [1], {})],
    ...     2: [(1, [2], {'fold-id': 'foo'}), (3, [2], {'fold-id': 'foo'}), (4, [2], {'fold-id': 'foo'})],
    ...     5: [(2, [5], {})],
    ...     6: [(5, [6], {})],
    ... }))
    [((0,), {})]
    >>> boop()
    False
    """
    stack = [node]
    seen = set(stack)
    markers = set()

    while stack:
        current = stack.pop()
        currentpreds = predecessors.get(current, ())

        # Get all fold-related markers for current node, they either get added
        # to the rest of markers XXX or they all get discarded XXX ???
        foldmarkers = {
            pred for pred in currentpreds
            if any(v for (k, v) in pred[3] if k == b'fold-id')
        }

        for pred in currentpreds:
            prednode = pred[0]

            if pred not in foldmarkers:
                markers.add(pred)

            # Basic cycle protection
            if prednode in seen:
                continue
            seen.add(prednode)

            if prednode in repo:
                yield (prednode,), markers | foldmarkers
                markers = set()
            else:
                stack.append(prednode)
