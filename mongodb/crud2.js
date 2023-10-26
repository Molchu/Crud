rs.initiate( {
    _id : "crud2",
    members: [
        { _id: 0, host: "cruddb2-0:27017"},
        { _id: 1, host: "cruddb2-1:27017"},
        { _id: 2, host: "cruddb2-2:27017"}
    ]
});