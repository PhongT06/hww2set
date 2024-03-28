#1
def compare_routes(our_routes, competitor_routes):

    common_dest = our_routes & competitor_routes
    unique_dest_ours = our_routes - competitor_routes
    unique_dest_competitor = competitor_routes - our_routes
    shared_dest = our_routes | competitor_routes
    
    print("Both airlines fly to:", common_dest)
    print("Only our airline flies to:", unique_dest_ours)
    print("Only competitor airline flies to:", unique_dest_competitor)
    print("Destinations shared by both airlines:", shared_dest)

# Example flight route data
our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

# Compare flight routes
compare_routes(our_routes, competitor_routes)


#2############################################################

no_dups = set()
customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]
for id in customer_ids:
    no_dups.add(id)
print(no_dups)



