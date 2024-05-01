package com.testefront.demo.service;

import com.testefront.demo.repository.BrokerIntegration;
import com.testefront.demo.repository.BrokerRequest;
import com.testefront.demo.repository.DeviceResponse;
import feign.FeignException;
import feign.RetryableException;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatusCode;
import org.springframework.stereotype.Service;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.Date;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

@Service
public class BrokerService {

    @Autowired
    private BrokerIntegration brokerIntegration;

    @Autowired
    private static Set<String> devices = new HashSet<>();


    public Set<String> getDevices(){
        try{
            var response = brokerIntegration.getDevices();
            if(response.getStatusCode().is2xxSuccessful()){
                var deviceResponse = response.getBody().getDevices();
                devices.addAll(deviceResponse);
            }
        }catch (RetryableException exception){
            System.out.println("Não foi possível se comunicar com o broker");
            return new HashSet<>();
        }



       return devices;
    }



    public String getState(int device) throws Exception {
        try{
            var deviceName = buildDevices(device);
            var state = brokerIntegration.getState(deviceName);
            return getMessage(state.getBody());

        }catch (FeignException e){
            return "Não foi possível verificar o estado atual do dispositivo. Tente novamente mais tarde.";
        }

    }

    public String updateState(int device, int speed) throws Exception {
        try{
            var deviceName = buildDevices(device);
            var request = BrokerRequest.builder()
                    .deviceName(deviceName)
                    .newSpeed(String.valueOf(speed))
                    .build();
            var state = brokerIntegration.updateState(request);
            if(state.getStatusCode().is2xxSuccessful()){
                return getMessage(state.getBody());}

            return getMessageDeviceError(state.getBody());

        }catch (FeignException e){
            return "Não foi possível atualizar o dispositivo";
        }

    }

    private String getMessageDeviceError(DeviceResponse body) {
        return "Não foi possível verificar o estado atual do dispositivo. Tente novamente mais tarde.";
    }

    private String getMessage(DeviceResponse device){
        DateTimeFormatter amPmFormatter = DateTimeFormatter.ofPattern("dd/MM/yyyy hh:mm:ss a");
        var actualHour = LocalDateTime.now().format(amPmFormatter);
        var commonMessage = "Estado atual do " + device.getName() + "   Ultima atualizacao:" + actualHour
                +"\nVelocidade: " + device.getSpeed()
                + "\nConsumo: " + device.getConsumption();
        var deviceOff = "O dispositivo está desligado. Consumo atual: "
                + device.getConsumption();


        return device.getSpeed().equals("0") ? deviceOff:commonMessage;
    }

    private String buildDevices(int device) throws Exception {
        List<String> deviceList = devices.stream().toList();
        try{
            return deviceList.get(device-1);
        }catch (Exception e){
            throw new Exception("Dispositivo inválido.");
        }

    }

    public Set<String> devices(){
        return devices;
    }
}
