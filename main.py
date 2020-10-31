if __name__ == "__main__":
    from loopr.client import LooprClient
    client = LooprClient()
    project =client.create_project(type="object_detection", name="object-detection-test",slug="object-de3eetessscssstion-test",configuration={
    "labels": [{"name": "bird", "tool": "bbox", "color": "#000000"}],
    "attributes": [],
})
    print(project.export_configuration())
    print(project)
    project.delete()
    dataset = client.create_dataset(type="image", name="image-data",slug="imagsssee-data")
    print(dataset)
    dataset.delete()
    datasets = client.get_datasets()
    for i in datasets:
        print(i)