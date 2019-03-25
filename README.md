# MasterPy

Generate a python node equipped for federation in a service mesh. Contributors welcome, just make a pull request.

## Installation

```python
  pip install git+git://github.com/ericsteen/master_py.git
```

## Roadmap

- [ ] CodeGen Bootstrap: [pymultigen](https://github.com/moltob/pymultigen/)
- [ ] Flask Blueprints, functional/divisional option

## Aim High

Refine generation schematics for evolvable service mesh architectures with MultiCloud [GitOps](https://www.weave.works/technologies/gitops/) as first class citizen for resiliency and [efficiency](https://www.amazon.com/Accelerate-Software-Performing-Technology-Organizations/dp/1942788339).

> An evolutionary architecture supports guided, incremental change across multiple dimensions – *Ford, Neal, Parsons, Rebecca, Kua, Patrick. [Building Evolutionary Architectures: Support Constant Change](https://www.thoughtworks.com/insights/blog/microservices-evolutionary-architecture). O'Reilly Media.*

###### MasterPy Key Dimensions:
  1. Flexibility (support many activities)
  2. Securability
  3. Observability
  4. Extensibility (support third-party strategies)

#### Application Plane
- **Thematic service generation, design patterns**:
  - General Data Processing
  - AI services
- **Key Python capabilities**:
  - **Core**: _numpy, scipy, pandas_
  - **Visualisation**: _matplotlib, seaborn, bokeh, plotly_
  - **Machine Learning**: _scikit-learn, keras, tensorflow, theano_
  - **NLP**: _nltk, gensim_
  - **Mining, Stats**: _scrapy, statsmodels_
- **CRD**'s (Custom Resource Definitions)

#### Control Plane
  - Security, Observability: [istio](https://istio.io/), [jaeger](https://www.jaegertracing.io/), [prometheus](https://github.com/deadtrickster/prometheus.erl).

#### Data Plane
  - Envoy + [ParallelPython](https://www.parallelpython.com/)


### Resources & Inspiration

#### Service Mesh
- [Understanding Microservices & Service Mesh](https://medium.com/microservices-learning/understanding-microservices-communication-and-service-mesh-e888d1adc41)
- [What is a Service Mesh?](https://glasnostic.com/blog/what-is-a-service-mesh-istio-linkerd-envoy-consul)


#### Code Generation
- Frederico Tomassetti [A Guide to Code Generation](https://tomassetti.me/code-generation/)

## Features

##### Application Plane Custom Resource Generation Toolkit

##### Data Plane Bootstrapping

##### Control Plane Bootstrapping

## Example Configuration

### _Coming Soon!_

## Strategy Configuration

### _Coming Soon!_

## Third Party Strategies

### _Coming Soon!_

## Testing
1. clone [master_py](https://github.com/ericsteen/master_py) into a dir
2. `export MPY=/path/to/dir` where MP is your custom env var
3. run the below shell function, replacing project name for your desired functionality

```bash
test_mpy() {
  cd $MPY;
}
```

## License

Apache 2.0. See [LICENSE.md](LICENSE.md) for details.
