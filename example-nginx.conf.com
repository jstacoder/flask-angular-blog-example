upstream flask-example {
    server unix:/tmp/nginx-example-blog.sock fail_timeout=0;
    # for a load balancer setup, run apps on 
    # the ports below, and uncomment
    #ip_hash;
    #server 127.0.0.1:4411 fail_timeout=0;
    #server 127.0.0.1:4412 fail_timeout=0;
    #server 127.0.0.1:4413 fail_timeout=0;
    #server 127.0.0.1:4414 fail_timeout=0;
    #server 127.0.0.1:4415 fail_timeout=0;
    #server 127.0.0.1:4416 fail_timeout=0;
}


server {
    listen 80;
    root /root/projects/github/flask-angular-blog-example/phlaskr;

    server_name flask-example.com;
    keepalive_timeout 2;

    access_log flask-example.log combined;
    error_log flask-example.log;

    location / {
        try_files $uri @phlaskr;
    }

    location @phlaskr {
        proxy_redirect off;
        proxy_set_header Host $http_host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Host $server_name;
        proxy_pass http://flask-example;
    }  
}


