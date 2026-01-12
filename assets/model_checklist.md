## Bronze

### Visualisations

Visualise the following:

- [ ] Arrivals over time (using a dotplot or heatmap).
- [ ] Resource use over time (overall as a line plot, plus recurrently at relevant timescale if recurrent patterns of resource use at).
- [ ] Distributions of generated activity times.
- [ ] Distributions of generated inter-arrival times.
- [ ] Queue lengths over time.

### Core Logic Checks

- [ ] Watch the journey of several individuals (via logs or animations).
- [ ] Check that all described stages demonstrate at least some activity during a sufficiently long, representative run.
- [ ] Add a random seed to the model, then test it by running the model twice with the same seed, and confirming that the results do not change by visually checking outputs.
- [ ] Manually check that the number of entities entering the model equals the number of leaving the model plus the number still in the model. This ensures no entities are "lost" in queues with no output no sink.
- [ ] Manually check that entities are never in two places at once.
- [ ] Manually check that resources are never simultaneously in use by two entities at once (or whatever variation is appropriate for your model).
- [ ] Outputs are being derived from a minimum of 30 runs (ideally more).
- [ ] Warm up length visually checked to be appropriate.
- [ ] Manually review that time units have been used consistently throughout the code (e.g. time inputs don't swap from minutes to hours at any point).
- [ ] Manually check logs to ensure that resources are not used at times where they should be obstructed/unavailable (e.g. during breaks, evenings, weekends).

### Key checks against the real system

- [ ] Number of entities arriving in simulation verified against historical patterns (averages sensible, distributions sensible).
    - [ ] If relevant, this is also checked for entity subtypes/entities with different attributes where it is important that these patterns match the real system.
- [ ] Generated activity times visually verified (averages sensible, distribution sensible).
    - [ ] If relevant, this is also checked for entity subtypes/entities with different attributes where it is important that these patterns match the real system.
- [ ] Visual check that there are no implausible activity lengths, with a cap applied if necessary to resolve this.
- [ ] Visual check that there are no implausible inter-arrival times for entities, with a cap applied if necessary to resolve this.
- [ ] Visual check of KPI outputs against the historical baseline - do these look sensible and similar to historical data?

### Process and Stakeholder Checks

- [ ] Approve the simulation process map with stakeholders.
- [ ] Check the scenario outputs with stakeholders - do they feel reasonable?
    - Note that stakeholder responses to outputs shouldn't necessarily be taken as a definite right/wrong judgment on the model - but they may help to sense check or indicate areas for more attention.

### Documentation

- [ ] Write a readme that explains how to run the model and gives a brief overview of the system being modelled.
- [ ] Include sufficient comments in your work to help people understand non-obvious elements of the code.
- [ ] Clearly document
    - [ ] data sources
    - [ ] assumptions
    - [ ] inputs
    - [ ] decisions - including any changes to the analytical plan or decisions made during analysis

## Silver

### Model Robustness

- [ ] Undertake sensitivity analysis.

### Documentation

- [ ] Add docstrings.
- [ ] Complete a formal model reporting checklist (e.g STRESS-DES).

### Code Review

- [ ] Have a code review undertaken by someone else (see [the DES RAP book: peer review](https://pythonhealthdatascience.github.io/des_rap_book/pages/guide/sharing/peer_review.html)).

### Automated Testing

Define formal automated tests:

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

- [ ] Meet the core requirements of the STARS reusability framework:
    - [ ] Open Licence
    - [ ] Dependency Management
    - [ ] Free and Open Source Model
    - [ ] Minimum Documentation
    - [ ] Research artifact metadata
    - [ ] Remote Code Repository
    - [ ] Open Science Archive

### Version Control

- [ ] Use version control for code (Git)

## Gold

### Documentation

- [ ] Documentation site created.
- [ ] Set up and maintain a changelog.

### Reusability

- [ ] Complete some or all of the optional elements of the STARS reusability framework:
    - [ ] Hosted Web App
    - [ ] Hosted Documentation
    - [ ] Online Coding Environment
    - [ ] Enhanced Documentation
    - [ ] Model Interface

### Model Efficiency

- [ ] Parallelisation implemented.

### Model Communication and Validation

- [ ] Animated model output created (if appropriate).
    - Animations also have a role to play in model validation - inspecting the animation, including with non-technical stakeholders, can help identify subtle bugs.

### Best Practice around Variability and Model Setup

- [ ] Formal method used for determining warm-up period.
- [ ] Formal method used for determining appropriate replication count.

### Automated Testing

- [ ] Define formal automated tests for:
    - [ ] Comparison of base case outputs to historical data for key metrics.
    - [ ] Statistical testing of generated distributions against real-world data (e.g. Kolgomorov-Smirnov Test).
