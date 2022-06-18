from asyncio import Task
from flask import Flask ,jsonify,request

app=Flask(__name__)

List=[
    {
        "id":1,
        "Name":"Samanyu",
        "Contact":"9611550306",
        "done":False

    },
    {
        "id":2,
        "Name":"Saju",
        "Contact":"9900105805",
        "done":False
    }
]

@app.route("/get-data")
def get_task():
    return jsonify({
        "data":List

    })

@app.route("/add-data",methods=["POST"])
def add_task():
    if not request.json:
        
        return jsonify({
            "status":"error",
            "message":"please provide data"
        },400)
    contact={
        "id":List[-1]['id']+1,
        "Name":request.json['Name'],
        "Contact":request.json.get('Contact',""),
        "done":False
    }   
    List.append(contact)    
    return jsonify({
        "status":"success",
        "message":"contact added successfully"
    })

if(__name__=="__main__"):
    app.run(debug=True)
        
            
        


