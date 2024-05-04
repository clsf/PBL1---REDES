package com.testefront.demo.repository;

import com.testefront.demo.config.feign.FeignConfiguration;
import org.springframework.cloud.openfeign.FeignClient;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;

@FeignClient(url = "${feign.client.config.broker.url}", configuration = FeignConfiguration.class,
        name = "broker")
public interface BrokerIntegration {

    //PEGA O ESTADO ATUAL DO DISPOSITIVO
    @GetMapping("/getState/{deviceName}")
    ResponseEntity<DeviceResponse> getState(
            @PathVariable("deviceName") String device
    );

    //ATUALIZA O DISPOSITIVO COM NOVAS INFORMAÇÕES
    @PostMapping("/update")
    ResponseEntity<DeviceResponse> updateState(
            @RequestBody BrokerRequest request
    );

    //PEGA LISTA DE DISPOSITIVOS DISPONIVEIS NO BROKER
    @GetMapping("/devices")
    ResponseEntity<DevicesResponse> getDevices();
}
