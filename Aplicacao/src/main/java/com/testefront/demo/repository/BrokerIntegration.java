package com.testefront.demo.repository;

import com.testefront.demo.config.feign.ClientResponse;
import com.testefront.demo.config.feign.ClientResponseDecoder;
import com.testefront.demo.config.feign.FeignConfiguration;
import org.springframework.cloud.openfeign.FeignClient;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@FeignClient(url = "${feign.client.config.broker.url}", configuration = FeignConfiguration.class,
        name = "broker")
public interface BrokerIntegration {

    @GetMapping("/test")
    String getTest();

    @GetMapping("/getState/{deviceName}")
    ResponseEntity<DeviceResponse> getState(
            @PathVariable("deviceName") String device
    );

    @PostMapping("/update")
    ResponseEntity<DeviceResponse> updateState(
            @RequestBody BrokerRequest request
    );

    @GetMapping("/devices")
    ResponseEntity<DevicesResponse> getDevices();
}
