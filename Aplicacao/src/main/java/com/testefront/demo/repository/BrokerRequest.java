package com.testefront.demo.repository;


import lombok.Builder;
import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
@Builder
public class BrokerRequest {

    private String deviceName;
    private String newSpeed;
}
