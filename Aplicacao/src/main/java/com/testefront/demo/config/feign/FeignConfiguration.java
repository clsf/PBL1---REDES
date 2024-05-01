package com.testefront.demo.config.feign;

import com.fasterxml.jackson.databind.ObjectMapper;
import feign.Request;
import feign.RequestInterceptor;
import feign.RequestTemplate;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class FeignConfiguration {

    @Bean
    public RequestInterceptor acceptInterceptor() {
        return new RequestInterceptor() {
            @Override
            public void apply(RequestTemplate template) {
                template.header("Accept", "application/json");
            }
        };
    }

    @Bean
    public Request.Options feignOptions() {
        return new Request.Options(2000, 5000);  // 2 segundos para conexão, 5 segundos para leitura
    }

//    @Bean
//    public ClientResponseDecoder clientResponseDecoder(ObjectMapper objectMapper){
//        return new ClientResponseDecoder(objectMapper);
//    }
}
