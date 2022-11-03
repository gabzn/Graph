Given a list of conversion rates and queries, find the exchange rate for each query.

Parameters:
    conversion rates: [['USD', 'JPY', 100], ['JPY', 'CHN', 20], ['CHN', 'THAI', 200], ['JPY', 'PESO', 5], ['PESO', 'CHN', 100], ['EURO', 'DOA', 50]]
                        1 USD is equal to 100 JPY
     
     queries: [['USD', 'CHN'], ['JPY', 'THAI'], ['USD', 'AUD'], ['THAI', 'PESO']]
                Find conversion rate from USD to CHN
          
def build_rate_graph(rates):
    rate_graph = defaultdict(set)

    for rate in rates:
        from_currency, to_currency, conversion_rate = rate

        target_rate = (to_currency, conversion_rate)
        rate_graph[from_currency].add(target_rate)

        inverse_target_rate = (from_currency, 1 / conversion_rate)
        rate_graph[to_currency].add(inverse_target_rate)

    return rate_graph

  
def find_conversion_rates(rates, queries):
    res = []
    rate_graph = build_rate_graph(rates)

    for query in queries:
        from_currency, to_currency = query
        find_conversion_rate(rate_graph, from_currency, to_currency, res)

    return res
  

# This will find the BEST conversion rate between f_currency to t_currency.
# Depends on the question asked, instead of finding the best rate, we can change it to just to find the rate.
def find_conversion_rate(rate_graph, f_currency, t_currency, res):    
    # If either currency is not on the graph, there's no way we can find the rate from one to the other.
    if f_currency not in rate_graph or t_currency not in rate_graph:
        res.append(-1.0)
        return

    """
    is_convertable tells us whether or not there's enough information to find the rate between
    f_currency to t_currency.

    It takes care of the case when both currencies exist in the graph, but there's simply not enough
    information to find the rate between them.
    """
    is_convertable = False
    rate = 1.0
    queue, visited_conversions = deque(), set()
    queue.append((f_currency, rate))

    while queue:
        current_currency, current_rate = queue.popleft()

        if current_currency == t_currency:
            is_convertable = True
            rate = max(current_rate, rate)

        for r in rate_graph[current_currency]:
            neighbour_c, n_rate = r
            """
            If we have already seen the conversion rate from current_currency to its neighbour currency,
            we don't need to look at it again.
            """
            if (current_currency, neighbour_c) in visited_conversions:
                continue

            visited_conversions.add((current_currency, neighbour_c))
            queue.append((neighbour_c, current_rate * n_rate))

    if is_convertable:
        res.append(rate)
    else:
        res.append(-1.0)
  

rates = [['USD', 'JPY', 100], ['JPY', 'CHN', 20], ['CHN', 'THAI', 200], ['JPY', 'PESO', 5], ['PESO', 'CHN', 100], ['EURO', 'DOA', 50]]
queries = [['USD', 'CHN'], ['JPY', 'THAI'], ['USD', 'AUD'], ['THAI', 'PESO']]
print(find_conversion_rates(rates, queries))
