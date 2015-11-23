

def logBranch(blocknumber,filename,linenumber):
    with open("test_create_block_coverage_log.txt", "a") as myfile:
        myfile.write("BlockNumber:"+str(blocknumber)+" File:"+filename+" LineNumber:"+str(linenumber)+"\n")

def clearTestLog():
    open("test_create_block_coverage_log.txt", 'w').close()
