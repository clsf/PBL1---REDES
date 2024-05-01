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

    @JsonProperty("devices")
    List<String> devices;
}
