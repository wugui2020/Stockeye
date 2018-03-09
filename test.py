from stockeye import watch

ticks = ['MSFT']

threshold = 3      # Number of recent articles published before an email is sent (default = 3)
hourspast = 18     # Define....recent (default = 18)
sentences = 3      # Length of summary generated for each article (deafult = 3)
firstlast = False  # Include first/last sentence of the artice in its summary (default = False)

watch([], ticks, [], threshold, hourspast, sentences, firstlast)
