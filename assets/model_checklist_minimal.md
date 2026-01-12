## Bronze

### Visualisations

*Creating simple visualisations of a few key areas is one of the best ways to spot unexpected behaviour and quickly validate key parts of your model logic. They allow you to quickly verify whether something looks unusually high or low, or if patterns are intuitively 'wrong'.*

Visualise the following:

- [ ] Arrivals over time
- [ ] Resource use over time
- [ ] Distributions of generated activity times **AND** generated inter-arrival times (one plot per activity or arrival generator).
- [ ] Queue lengths over time.

### Core Logic Checks

*When you are doing these checks, you are really just looking for something being 'off'.*

- [ ] Watch the journey of several individuals (via logs or animations).
- [ ] Review the code to check that time units have been used consistently throughout the code (e.g. time inputs don't swap from minutes to hours at any point).

*The following items can be robustly checked using [event logs](https://des.hsma.co.uk/event_logging.html).*

*However, you may be able to do some more basic checks with [console logs](https://des.hsma.co.uk/basic_debugging_tactics.html#using-simple-print-statements).*


- [ ] Check that all described stages demonstrate at least some activity during a sufficiently long, representative run.
- [ ] Manually check that the number of entities entering the model equals the number of leaving the model plus the number still in the model.
- [ ] Manually check that entities are never in two places at once.
- [ ] Manually check that resources are never simultaneously in use by two entities at once (or whatever variation is appropriate for your model).
- [ ] Manually check that resources are not used at times where they should be obstructed/unavailable (e.g. during breaks, evenings, weekends).

### Robustness for decision-making

- [ ] Number of runs set to a **minimum of 30** (ideally more) for generating any metrics or other outputs that will be used for decision-making.
- [ ] [Warm up length visually checked] to be appropriate(https://pythonhealthdatascience.github.io/des_rap_book/pages/guide/output_analysis/length_warmup.html).

### Reproducibility

- [ ] Add a random seed to the model, then test it by running the model twice with the same seed, and visually check outputs to confirm that the results do not change.

### Key checks against the real system

- [ ] Number of entities arriving in simulation verified against historical patterns (averages sensible, distributions sensible).
    - [ ] If relevant, this is also checked for entity subtypes/entities with different attributes where it is important that these patterns match the real system.
- [ ] Generated activity times visually verified (averages sensible, distribution sensible).
    - [ ] If relevant, this is also checked for entity subtypes/entities with different attributes where it is important that these patterns match the real system.
- [ ] Visual check that there are no implausible activity lengths.
    - [ ] If necessary, apply a cap to generated activity times to resolve this.
- [ ] Visual check that there are no implausible inter-arrival times for entities
    - [ ] If necessary, apply a cap to generated inter-arrival times to resolve this.
- [ ] Visual check of KPI outputs against the historical baseline - do these look sensible and similar to historical data?

### Process and Stakeholder Checks

- [ ] Approve the simulation process map with stakeholders.
- [ ] Check the scenario outputs with stakeholders - do they feel reasonable?

### Documentation

- [ ] Write a readme that explains how to run the model and gives a brief overview of the system being modelled.
- [ ] Include sufficient comments in your work to help people understand non-obvious elements of the code.
- [ ] Clearly document
    - [ ] data sources
    - [ ] assumptions
    - [ ] inputs
    - [ ] decisions - including any changes to the analytical plan or decisions made during analysis
- [ ] [Document the versions of packages you have used](https://des.hsma.co.uk/stars.html#dependency-management), ideally using a requirements.txt or environment.yml file.


## Silver

### Documentation

- [ ] Add [docstrings](https://hsma-programme.github.io/h6_march_2025_forum_presentation/#/making-your-code-super-readable-with-docstrings).
- [ ] Complete a formal model reporting checklist (e.g [STRESS-DES](https://des.hsma.co.uk/stress_des.html)).

### Code Review

- [ ] Have a code review undertaken by someone else (see [the DES RAP book: peer review](https://pythonhealthdatascience.github.io/des_rap_book/pages/guide/sharing/peer_review.html)).

### Automated Testing

Define [formal automated tests](https://des.hsma.co.uk/tests.html):

- [ ] Model running successfully.
- [ ] Varying results are obtained when using different seeds and the same parameters.
- [ ] Identical results are obtained when the same seed and parameters are used.
- [ ] Number of entities entering the model equals the number of leaving the model plus the number still in the model. This ensures no entities are "lost" in queues with no output no sink.
- [ ] Utilisation never exceeds capacity (i.e. resources are never in use by multiple entities, unless allowed in your model).
- [ ] All stages of the model show some activity (i.e. there are no 'orphaned' steps).
- [ ] Simple 'expected behaviour' when parameters are varied:
    - [ ] Longer activity time = worse performance.
    - [ ] More arrivals = longer queues.
- [ ] Write tests for behaviour under extreme conditions:
    - [ ] Heavy demand.
    - [ ] Little to no demand.

### Reusability

- [ ] Add an [Open Licence](https://des.hsma.co.uk/stars.html#open-licence) to your repository

### Version Control

- [ ] Use version control for code (Git)

### Model Robustness

- [ ] Undertake sensitivity analysis (i.e. check how much changes in model input variables affect output performance measures, and consider whether results appear sensible/expected)

## Gold

### Documentation

- [ ] [Create a documentation site and host this](https://des.hsma.co.uk/stars.html#documentation-hosting).
- [ ] [Set up and maintain a changelog](https://keepachangelog.com/en/1.1.0/).
- [ ] Use [GitHub Issues](https://hsma-programme.github.io/h6_march_2025_forum_presentation/#/github-issues) to document planned changes

### Reusability

- [ ] [Research artifact metadata (ORCID)](https://des.hsma.co.uk/stars.html#open-researcher-and-contributor-identifier-orcid)
- [ ] [Open Science Archive](https://des.hsma.co.uk/stars.html#open-science-archive)
- [ ] [Online Coding Environment](https://des.hsma.co.uk/stars.html#online-coding-environment)

### Model Efficiency

- [ ] [Parallelisation](https://des.hsma.co.uk/running_parallel_cpus.html) implemented.

### Model Communication and Validation

- [ ] [Create a web app interface for your model](https://des.hsma.co.uk/stars.html#model-interface)
- [ ] [Host the web app interface for your model](https://des.hsma.co.uk/stars.html#web-app-hosting)
- [ ] [Animated model output](https://hsma-tools.github.io/vidigi/vidigi_docs/adding_vidigi_to_a_simple_simpy_model_hsma_structure.html) created (if appropriate).

### Best Practice around Variability and Model Setup

- [ ] Formal automated method implemented for determining warm-up period.
- [ ] Formal method used for determining appropriate replication count.

### Automated Testing

- [ ] Define formal automated tests for:
    - [ ] Comparison of base case outputs to historical data for key metrics.
    - [ ] Statistical testing of generated distributions against real-world data (e.g. Kolgomorov-Smirnov Test).
