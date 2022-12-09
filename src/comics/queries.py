def get_previous_issue(current_issue):
    return get_issue_from_filtered_sorted_query_set(
        current_issue.arc, {"sort_order__lt": current_issue.sort_order}, "-sort_order"
    )


def get_next_issue(current_issue):
    return get_issue_from_filtered_sorted_query_set(
        current_issue.arc, {"sort_order__gt": current_issue.sort_order}, "sort_order"
    )


def get_issue_from_filtered_sorted_query_set(arc, filter_dict, sort_string):
    image = None

    try:
        # Reminder: the ** in front of the dict converts it to keyword args
        image = arc.issues.filter(**filter_dict).order_by(sort_string)[0]
    except IndexError:
        pass  # Don't worry about it

    return image
