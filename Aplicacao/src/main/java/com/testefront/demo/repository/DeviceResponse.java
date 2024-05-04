package com.testefront.demo.repository;

import lombok.Data;
import lombok.Getter;

@Data
@Getter
public class DeviceResponse {
    //CLASSE QUE DEFINE O OBJETO DE RESPOSTA
    private String name;
    private String speed;
    private String consumption;
}
