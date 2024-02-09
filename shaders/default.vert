#version 330 core

layout (location = 0) in vec2 in_texcoord_0; // where to put the texture
layout (location = 1) in vec3 in_normal;     // normal vectors for light
layout (location = 2) in vec3 in_position;   // vertex position data

out vec2 uv_0;
out vec3 normal;
out vec3 fragPos;

uniform mat4 m_proj;
uniform mat4 m_view;
uniform mat4 m_model;

void main() {
    uv_0 = in_texcoord_0;
    fragPos = vec3(m_model * vec4(in_position, 1.0));
    normal = mat3(transpose(inverse(m_model))) * normalize(in_normal);
    gl_Position = m_proj * m_view * m_model * vec4(in_position, 1.0);
}