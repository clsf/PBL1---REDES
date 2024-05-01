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

    @RequestMapping("/trigger-device")
    public String triggerDevice() {
        return brokerIntegration.getTest();
    }

//    @RequestMapping("/getDevice/{deviceName}")
//    public DeviceResponse getStateDevice(
//            @PathVariable("deviceName") String deviceName
//    ){
//        return brokerIntegration.getState(deviceName).getContent();
//    }
//
//    @RequestMapping("/devices")
//    public DevicesResponse getDevices(){
//        return brokerIntegration.getDevices().getContent();
//    }

//    @RequestMapping("/update")
//    public DeviceResponse updateDevice(
//            @RequestBody BrokerRequest request
//            ){
//        return brokerIntegration.updateState(request).getContent();
//    }
}
