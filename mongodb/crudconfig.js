rs.initiate( {
    _id : "crudconfig",
    members: [
        { _id: 0, host: "cruddb-config-0:27017"},
        { _id: 1, host: "cruddb-config-1:27017"},
        { _id: 2, host: "cruddb-config-2:27017"}
    ]
});