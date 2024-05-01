package com.testefront.demo.config.feign;

import com.fasterxml.jackson.annotation.JsonUnwrapped;
import lombok.Getter;
import lombok.NoArgsConstructor;

@Getter
@NoArgsConstructor
public class ClientResponse<T> {
    @JsonUnwrapped
    private T content;

    public ClientResponse(T content){
        this.content = content;
    }
}
