;;
;; This is default bootstrap file for Grapher
;;

(deftemplate SQLITEDB
    (slot dbpath)
    (slot dbname
        (type STRING)
        (default "GRAPHER.db")
    )
    (slot schemapath)
    (slot is_open
        (default FALSE)
    )
)
