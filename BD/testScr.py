from operations_BD  import SqlliteDB

SqlliteDB.insertData('source_1', 'description_1', '2023-01-01')
SqlliteDB.insertData('source_2', 'description_2', '2023-02-02')
SqlliteDB.insertData('source_3', 'description_3', '2023-03-03')
SqlliteDB.insertData('source_4', 'description_4', '2023-04-04')
SqlliteDB.insertData('source_5', 'description_5', '2023-05-05')

#result_by_id = SqlliteDB.selectDataByID(20)
#print('byId')
#print(result_by_id)
#result_by_source= SqlliteDB.selectDataBySource('source_5')
#print('Bysource')
#print(result_by_source)

#print("lastlogs")
result= SqlliteDB.selectLastLogs(4)
#for row in result:
#    print(row)
print(result)




