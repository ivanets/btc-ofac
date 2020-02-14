# bitcoin_OFAC

This is a simple Python program that uses a couple libraries to scrape the SDN List for crypto addresses. 
The structure of this script is based on the description used in this FAQ from the US Department of Tresury:

563. What is the structure of a digital currency address on OFAC’s SDN List?

Digital currency addresses listed on the SDN List include their unique alphanumeric identifier (up to 256 characters) and identify the digital currency to which the address corresponds (e.g., Bitcoin (XBT), Ethereum (ETH), Litecoin (LTC), Neo (NEO), Dash (DASH), Ripple (XRP), Iota (MIOTA), Monero (XMR), and Petro (PTR)). Each digital currency address listed on the SDN list will have its own field: the structure will always begin with “Digital Currency Address”, followed by a dash and the digital currency’s symbol (e.g., “Digital Currency Address - XBT”, “Digital Currency Address - ETH”). This information is followed by the unique alphanumeric identifier of the specific address. [06-06-2018]

Using this description, the script is executed based on the assumption that the string "Digital Currency Address" is a precursor to every crypto address added to the SDN List. Thus, if the assumption remains true, this program should be able to pull any crypto address from the List agnostically.
