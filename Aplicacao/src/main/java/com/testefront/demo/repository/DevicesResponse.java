package com.testefront.demo.repository;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.Data;
import lombok.Getter;

import java.util.List;

@Getter
@Data
@JsonIgnoreProperties(ignoreUnknown = true)
public class DevicesResponse {
    //CLASSE QUE DEFINE O OBJETO DE RESPOSTA, NO CASO UMA LISTA DE DEVICES
    @JsonProperty("devices")
    List<String> devices;
}
