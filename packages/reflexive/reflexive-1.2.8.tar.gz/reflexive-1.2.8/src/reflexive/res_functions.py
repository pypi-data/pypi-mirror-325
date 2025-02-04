# import text into dataframe
# accepts either an iterable of strings, or an iterable over text files
# returns a pandas series iterable of type string

# clean text and calculate length
# accepts an iterable of strings in form of pandas series of type string
# returns a pandas series iterable of type int


# chunk text and keep original index ref
# accepts an iterable of dataframe rows
# returns an iterable of dataframe rows with added column 'text_chunks' - list of strings

# upload docs to s3 and save local copy - side effects
# accepts an iterable of iterable of chunks (with ids)
# returns an an iterable of s3 responses? URLs to S3 file?

# initiate custom entity job on comprehend
# no parameters
# returns job id for checking status, and downloading

# check status
# accepts job id
# returns status

# download results
# accepts job id
# returns iterable of results

# unpack results and load into dataframe


# extract reflexive expressions into dataframe


# get reflexive sequences


# get interactions


# create count adj matrix


# create weighted adj matrix


# save dataframe to file


# visualise expressions in text


# visualise reflexive sequence


# visualise res graph


#
# Network analysis functions
#