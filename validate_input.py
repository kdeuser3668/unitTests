def validate_input(symbol, chart_type, time_series, start_date, end_date):
    # Validate symbol
    if not symbol.isalpha() or not symbol.isupper() or len(symbol) > 7:
        return False

    # Validate chart type
    if chart_type not in ['1', '2']:
        return False

    # Validate time series
    if time_series not in ['1', '2', '3', '4']:
        return False

    # Validate start date
    try:
        datetime.datetime.strptime(start_date, '%Y-%m-%d')
    except ValueError:
        return False

    # Validate end date
    try:
        datetime.datetime.strptime(end_date, '%Y-%m-%d')
    except ValueError:
        return False

    return True