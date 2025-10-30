package com.ecologistics;

import org.apache.camel.dataformat.bindy.annotation.CsvRecord;
import org.apache.camel.dataformat.bindy.annotation.DataField;

@CsvRecord(separator = ",", skipFirstLine = true, generateHeaderColumns = true)
public class Envio {

    @DataField(pos = 1, columnName = "id_envio")
    private String id_envio;

    @DataField(pos = 2, columnName = "cliente")
    private String cliente;

    @DataField(pos = 3, columnName = "direccion")
    private String direccion;

    @DataField(pos = 4, columnName = "estado")
    private String estado;

    public String getId_envio() { return id_envio; }
    public void setId_envio(String id_envio) { this.id_envio = id_envio; }

    public String getCliente() { return cliente; }
    public void setCliente(String cliente) { this.cliente = cliente; }

    public String getDireccion() { return direccion; }
    public void setDireccion(String direccion) { this.direccion = direccion; }

    public String getEstado() { return estado; }
    public void setEstado(String estado) { this.estado = estado; }
}
