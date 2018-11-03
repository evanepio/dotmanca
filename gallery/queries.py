def get_previous_image(gallery, sort_order):
    return get_image_from_filtered_sorted_query_set(
        gallery, {"sort_order__lt": sort_order}, "-sort_order"
    )


def get_next_image(gallery, sort_order):
    return get_image_from_filtered_sorted_query_set(
        gallery, {"sort_order__gt": sort_order}, "sort_order"
    )


def get_image_from_filtered_sorted_query_set(gallery, filter_dict, sort_string):
    image = None

    try:
        # Reminder: the ** in front of the dict converts it to keyword args
        image = gallery.images.filter(**filter_dict).order_by(sort_string)[0]
    except IndexError:
        pass  # Don't worry about it

    return image
