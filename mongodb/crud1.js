rs.initiate( {
    _id : "crud1",
    members: [
        { _id: 0, host: "cruddb1-0:27017"},
        { _id: 1, host: "cruddb1-1:27017"},
        { _id: 2, host: "cruddb1-2:27017"}
    ]
});