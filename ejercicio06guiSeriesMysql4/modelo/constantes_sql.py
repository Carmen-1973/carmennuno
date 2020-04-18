SQL_INSERCION_SERIE = "INSERT INTO `tabla_series` (`titulo`, `sinopsis`, `temporadas`, `fecha_lanzamiento`, `vista_si_no`) VALUES (%s, %s, %s, %s, %s);"
SQL_LISTADO_SERIES = "SELECT * FROM tabla_series"
SQL_BORRAR_SERIE = "DELETE FROM tabla_series WHERE id = %s ;"
SQL_OBTENER_SERIE_POR_ID = "SELECT * FROM tabla_series WHERE id = %s ;"
SQL_GUARDAR_CAMBIOS_SERIE = "UPDATE tabla_series SET titulo = %s , sinopsis = %s , temporadas = %s , fecha_lanzamiento = %s , vista_si_no = %s WHERE id = %s ;"

