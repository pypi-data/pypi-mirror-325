import subprocess

def scale_kubernetes_services():
    services = {
        "onc-monitoring-service": "kubectl --kubeconfig=/etc/kubernetes/admin.conf scale sts monitoring -n onc --replicas=0",
        "onc-alarm-service": "kubectl --kubeconfig=/etc/kubernetes/admin.conf scale sts onc-alarm-service -n onc --replicas=0",
        "onc-apps-ui-service": "kubectl --kubeconfig=/etc/kubernetes/admin.conf scale deploy onc-apps-ui-service -n onc --replicas=0",
        "onc-circuit-service": "kubectl --kubeconfig=/etc/kubernetes/admin.conf scale sts onc-circuit-service -n onc --replicas=0",
        "onc-collector-service": "kubectl --kubeconfig=/etc/kubernetes/admin.conf scale sts onc-collector-service -n onc --replicas=0",
        "onc-config-service": "kubectl --kubeconfig=/etc/kubernetes/admin.conf scale sts onc-config-service -n onc --replicas=0",
        "onc-devicemanager-service": "kubectl --kubeconfig=/etc/kubernetes/admin.conf scale sts onc-devicemanager-service -n onc --replicas=0",
        "onc-inventory-service": "kubectl --kubeconfig=/etc/kubernetes/admin.conf scale sts onc-inventory-service -n onc --replicas=0",
        "onc-nbi-service": "kubectl --kubeconfig=/etc/kubernetes/admin.conf scale sts onc-nbi-service -n onc --replicas=0",
        "onc-netconfcollector-service": "kubectl --kubeconfig=/etc/kubernetes/admin.conf scale deploy onc-netconfcollector-service -n onc --replicas=0",
        "onc-osapi-gw-service": "kubectl --kubeconfig=/etc/kubernetes/admin.conf scale sts onc-osapi-gw-service -n onc --replicas=0",
        "onc-pce-service": "kubectl --kubeconfig=/etc/kubernetes/admin.conf scale sts onc-pce-service -n onc --replicas=0",
        "onc-pm-service": "kubectl --kubeconfig=/etc/kubernetes/admin.conf scale sts onc-pm-service -n onc --replicas=0",
        "onc-pmcollector-service": "kubectl --kubeconfig=/etc/kubernetes/admin.conf scale deploy onc-pmcollector-service -n onc --replicas=0",
        "onc-topology-service": "kubectl --kubeconfig=/etc/kubernetes/admin.conf scale sts onc-topology-service -n onc --replicas=0",
        "onc-torch-service": "kubectl --kubeconfig=/etc/kubernetes/admin.conf scale sts onc-torch-service -n onc --replicas=0",
    }
    
    print("Starting Kubernetes scaling script...")
    exclude_service = input("Enter the service name to exclude: ").strip()
    print(f"User requested to exclude: {exclude_service}")
    
    for service, cmd in services.items():
        if service == exclude_service:
            print(f"Skipping: {service}")
            continue
        try:
            print(f"Executing command for: {service}")
            subprocess.run(cmd, shell=True, check=True)
            print(f"Successfully executed: {cmd}")
        except subprocess.CalledProcessError as e:
            print(f"Error executing command for {service}: {cmd}\nError: {e}")
    
    print("Kubernetes scaling script completed.")

if __name__ == "__main__":
    scale_kubernetes_services()