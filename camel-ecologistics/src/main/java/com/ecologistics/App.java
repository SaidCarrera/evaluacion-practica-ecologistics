package com.ecologistics;

import org.apache.camel.main.Main;

public class App {

    public static void main(String[] args) throws Exception {
        Main main = new Main();
        main.configure().addRoutesBuilder(new Routes());
        System.out.println("[INFO] Aplicación Camel iniciada. Esperando archivos CSV en data/in/");
        main.run();
    }
}
