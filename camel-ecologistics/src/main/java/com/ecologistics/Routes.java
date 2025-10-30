package com.ecologistics;

import org.apache.camel.builder.RouteBuilder;
import org.apache.camel.model.dataformat.BindyType;

public class Routes extends RouteBuilder {
    @Override
    public void configure() throws Exception {

        from("file:data/in?noop=true")
            .routeId("csv-to-json-route")
            .log("[INFO] Archivo CSV detectado: ${file:name}")
            .unmarshal().bindy(BindyType.Csv, Envio.class)
            .marshal().json()
            .log("[INFO] Datos transformados a JSON: ${body}")
            .to("file:data/out?fileName=envios.json")
            .log("[INFO] Archivo JSON generado exitosamente en data/out/envios.json");
    }
}
