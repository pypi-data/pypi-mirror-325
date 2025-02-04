from math import ceil


def ChunksForRange(
    *,
    start: int = 0,
    end: int | None = None,
    end_p_1: int | None = None,
    n_elements: int | None = None,
    n_chunks: int | None = None,
    chunk_size: int | None = None,
    return_bounds_only: bool = True,
    bound_end_should_be_p_1: bool = True,
) -> tuple[tuple[int, int], ...] | tuple[tuple[int, ...], ...]:
    """"""
    if n_elements is not None:
        end_p_1 = start + n_elements
    elif end_p_1 is not None:
        n_elements = end_p_1 - start
    elif end is not None:
        end_p_1 = end + 1
        n_elements = end_p_1 - start
    else:
        raise ValueError(
            'One argument must not be None among "n_elements", "end_p_1", and "end".'
        )

    if n_chunks is not None:
        assert n_chunks <= n_elements
        chunk_size = int(ceil(n_elements / n_chunks))
        # should_even_chunks = True
    else:
        assert (chunk_size is not None) and (chunk_size <= n_elements)
        # should_even_chunks = False

    if return_bounds_only and not bound_end_should_be_p_1:
        end_offset = -1
    else:
        end_offset = 0
    bounds = tuple(
        (_, min(_ + chunk_size, end_p_1) + end_offset)
        for _ in range(start, end_p_1, chunk_size)
    )

    if return_bounds_only:
        return bounds

    return tuple(tuple(range(_stt, _end)) for _stt, _end in bounds)
