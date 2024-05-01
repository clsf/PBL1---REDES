package com.testefront.demo.repository;

import lombok.Data;
import lombok.Getter;

@Data
@Getter
public class DeviceResponse {

    private String name;
    private String speed;
    private String consumption;
}
