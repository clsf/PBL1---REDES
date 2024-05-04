package com.testefront.demo.controller;


import com.testefront.demo.repository.BrokerIntegration;
import com.testefront.demo.repository.BrokerRequest;
import com.testefront.demo.repository.DeviceResponse;
import com.testefront.demo.repository.DevicesResponse;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class ApplicationController {

    @Autowired
    private BrokerIntegration brokerIntegration;


    @RequestMapping("/getDevice/{deviceName}")
    public DeviceResponse getStateDevice(
            @PathVariable("deviceName") String deviceName
    ){
        return brokerIntegration.getState(deviceName).getBody();
    }

    @RequestMapping("/devices")
    public DevicesResponse getDevices(){
        return brokerIntegration.getDevices().getBody();
    }

    @RequestMapping("/update")
    public DeviceResponse updateDevice(
            @RequestBody BrokerRequest request
            ){
        return brokerIntegration.updateState(request).getBody();
    }
}
