def get_previous_image(gallery_image):
    return get_image_from_filtered_sorted_query_set(
        gallery_image.gallery,
        {"sort_order__lt": gallery_image.sort_order},
        "-sort_order",
    )


def get_next_image(gallery_image):
    return get_image_from_filtered_sorted_query_set(
        gallery_image.gallery,
        {"sort_order__gt": gallery_image.sort_order},
        "sort_order",
    )


def get_image_from_filtered_sorted_query_set(gallery, filter_dict, sort_string):
    image = None

    try:
        # Reminder: the ** in front of the dict converts it to keyword args
        image = gallery.images.filter(**filter_dict).order_by(sort_string)[0]
    except IndexError:
        pass  # Don't worry about it

    return image
