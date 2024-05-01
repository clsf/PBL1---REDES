package com.testefront.demo.config.feign;

import com.fasterxml.jackson.databind.JavaType;
import com.fasterxml.jackson.databind.ObjectMapper;
import feign.FeignException;
import feign.Response;
import feign.codec.Decoder;
import lombok.extern.slf4j.Slf4j;
import org.apache.commons.io.IOUtils;

import java.io.IOException;
import java.lang.reflect.ParameterizedType;
import java.lang.reflect.Type;
import java.nio.charset.StandardCharsets;

@Slf4j
public class ClientResponseDecoder implements Decoder {

    public ClientResponseDecoder(ObjectMapper objectMapper) {
        this.mapper = objectMapper;
    }

    private final ObjectMapper mapper;

    @Override
    public Object decode(Response response, Type type) throws IOException, FeignException {
        Type consideredType = type;
        IOUtils.toString(response.body().asInputStream(), StandardCharsets.UTF_8);
        if (consideredType instanceof ParameterizedType pType && pType.getRawType().getTypeName().equalsIgnoreCase(ClientResponse.class.getCanonicalName())) {
            consideredType = pType.getActualTypeArguments()[0];

            if (isVoidType(consideredType)) {
                return new ClientResponse<>();
            }
            JavaType jt = mapper.getTypeFactory().constructType(consideredType);
            Object o = mapper.readValue(response.body().asReader(StandardCharsets.UTF_8), jt);
            return new ClientResponse<>(o);
        }


        JavaType jt = mapper.getTypeFactory().constructType(type);
        return mapper.readValue(response.body().asReader(StandardCharsets.UTF_8), jt);
    }

    boolean isVoidType(Type type) {
        return type.getTypeName().contains(Void.class.getSimpleName());
    }
}
