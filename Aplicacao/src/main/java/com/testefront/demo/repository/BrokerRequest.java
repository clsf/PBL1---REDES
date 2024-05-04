package com.testefront.demo.repository;


import lombok.Builder;
import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
@Builder
public class BrokerRequest {
    //CLASSE QUE DEFINE OBJETO DE REQUEST, INFORMAÇÕES PERTINENTES AO REQUEST
    private String deviceName;
    private String newSpeed;
}
