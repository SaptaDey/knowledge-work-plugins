---
name: bio-research
description: Complete life sciences research skill for clinical trial protocols, bioinformatics pipelines, single-cell analysis, scientific problem selection, and laboratory data standardization. Use when designing clinical trials, running nf-core pipelines, analyzing single-cell RNA-seq data, selecting research problems, or converting instrument data to standardized formats. Trigger phrases include "design a clinical trial for", "run the rnaseq pipeline", "analyze this single-cell data", "help me choose a research problem", "convert this instrument data", "QC this scRNA data".
---

# Bio-Research Skill

Accelerate early-stage life sciences R&D with tools for clinical trial design, bioinformatics, single-cell analysis, and research strategy.

## Core Capabilities

- **Clinical Trial Protocol**: Generate FDA/NIH-compliant protocols
- **Nextflow Pipelines**: Run nf-core bioinformatics pipelines
- **Single-Cell Analysis**: scvi-tools and QC workflows
- **Scientific Problem Selection**: Strategic research planning
- **Data Standardization**: Convert instrument data to Allotrope format

## Quick Commands

| Command | Usage | Description |
|---------|-------|-------------|
| `/start` | `/start` | Set up bio-research environment |

---

## Clinical Trial Protocol

### Modes

**Research Mode:**
- Literature review for similar trials
- FDA guidance identification
- Regulatory pathway assessment
- No protocol generation

**Protocol Mode:**
- Complete FDA/NIH-compliant protocol
- 6-phase modular generation
- Sample size calculations
- Regulatory submission ready

### Protocol Structure

```markdown
# Clinical Trial Protocol: [Study Title]

## 1. Title Page
- Protocol Number
- Sponsor
- Principal Investigator
- Version and Date

## 2. Synopsis
[1-2 page summary of the trial]

## 3. Background
- Disease/condition overview
- Current treatment landscape
- Rationale for intervention
- Nonclinical and clinical data

## 4. Objectives
### Primary
[Primary endpoint]

### Secondary
[Secondary endpoints]

### Exploratory
[Exploratory endpoints]

## 5. Study Design
- Design type (randomized, blinded, etc.)
- Treatment arms
- Duration
- Sample size with justification

## 6. Study Population
### Inclusion Criteria
### Exclusion Criteria

## 7. Intervention
- Description
- Dosing
- Administration
- Compliance monitoring

## 8. Assessments
- Efficacy assessments
- Safety assessments
- Schedule of events

## 9. Statistical Considerations
- Primary analysis
- Sample size calculation
- Missing data handling

## 10. Safety
- AE definitions
- SAE reporting
- DSMB charter

## 11. Ethics and Regulatory
- IRB/Ethics approval
- Informed consent
- Data privacy
```

### Regulatory Pathways

| Pathway | Use Case | Timeline |
|---------|----------|----------|
| Standard IND | Typical drug development | 30-day FDA review |
| Investigator IND | Academic research | 30-day FDA review |
| Emergency IND | Life-threatening situation | 24-hour response |
| 510(k) | Medical device, predicate exists | 90 days |
| De Novo | Novel low-risk device | 150 days |
| PMA | High-risk device | 180 days |

---

## Nextflow Pipelines

### Supported Pipelines

| Pipeline | Purpose | Input |
|----------|---------|-------|
| **rnaseq** | RNA sequencing analysis | FASTQ files |
| **sarek** | Variant calling (germline/somatic) | FASTQ or BAM |
| **atacseq** | Chromatin accessibility | FASTQ files |

### Setup Workflow

1. **Validate environment**: Check Nextflow, Java, container engine
2. **Run test profile**: Verify pipeline works
3. **Create samplesheet**: Format input files
4. **Configure genome**: Download or specify reference
5. **Execute pipeline**: Run with appropriate resources
6. **Verify outputs**: Check quality metrics

### Samplesheet Format

**RNA-seq:**
```csv
sample,fastq_1,fastq_2,strandedness
sample1,/path/to/sample1_R1.fastq.gz,/path/to/sample1_R2.fastq.gz,auto
```

**Sarek:**
```csv
patient,sample,lane,fastq_1,fastq_2
patient1,tumor,lane1,tumor_R1.fastq.gz,tumor_R2.fastq.gz
patient1,normal,lane1,normal_R1.fastq.gz,normal_R2.fastq.gz
```

### Common Commands

```bash
# Test run
nextflow run nf-core/rnaseq -profile test,docker

# Full run
nextflow run nf-core/rnaseq \
    --input samplesheet.csv \
    --outdir results \
    --genome GRCh38 \
    -profile docker
```

---

## Single-Cell Analysis

### scvi-tools Models

| Model | Application |
|-------|-------------|
| **scVI** | Integration, batch correction |
| **scANVI** | Label transfer with annotations |
| **totalVI** | CITE-seq (RNA + protein) |
| **PeakVI** | ATAC-seq peak analysis |
| **MultiVI** | Multiome (RNA + ATAC) |
| **DestVI** | Spatial deconvolution |
| **veloVI** | RNA velocity |

### Quality Control Workflow

**MAD-based Filtering:**
```python
# Standard thresholds
- n_genes_by_counts: 3 MAD below/above median
- total_counts: 3 MAD below/above median
- pct_counts_mt: 3 MAD above median (or fixed 20%)
```

**QC Metrics:**
- Genes detected per cell
- UMI counts per cell
- Mitochondrial percentage
- Doublet scores

### Output Format

```markdown
# Single-Cell QC Report

## Dataset Overview
| Metric | Before QC | After QC |
|--------|-----------|----------|
| Cells | N | N |
| Genes | N | N |
| Median genes/cell | N | N |
| Median UMIs/cell | N | N |

## Filtering Applied
- [Filter 1]: [Threshold]
- [Filter 2]: [Threshold]

## Visualizations
- Violin plots (genes, counts, mito%)
- Scatter plots (genes vs counts)
- Knee plots

## Recommendations
- [Next steps for analysis]
```

---

## Scientific Problem Selection

### Framework (Fischbach & Walsh Methodology)

**Entry Points:**
1. **Pitch new idea**: Evaluate potential
2. **Troubleshoot current project**: Assess continuation
3. **Ask strategic question**: Navigate research decisions

### Evaluation Dimensions

**Intuition Pumps:**
- Thought experiments for problem framing
- Analogies from other fields
- Edge case exploration

**Risk Assessment:**
- Technical risk (can it be done?)
- Impact risk (does it matter?)
- Execution risk (can you do it?)

**Optimization Function:**
- Define success metrics
- Weight competing priorities
- Set decision thresholds

**Parameter Strategy:**
- Identify key variables
- Design experiments to isolate effects
- Plan iteration cycles

### Decision Tree

```
Is the problem tractable?
├── No → Can you reduce scope? → No → Consider alternatives
├── Uncertain → Design validation experiment
└── Yes → Is impact sufficient?
    ├── No → Can you increase scope without adding risk?
    └── Yes → Proceed with implementation plan
```

### Adversity Planning

- Identify failure modes
- Develop contingency plans
- Set pivot triggers
- Build optionality

---

## Data Standardization

### Instrument Data to Allotrope

Convert laboratory instrument outputs to standardized Allotrope Simple Model (ASM) JSON format.

**Supported Instruments:**
- Plate readers (absorbance, fluorescence)
- Flow cytometers
- qPCR instruments
- Mass spectrometers
- Chromatography systems

### Conversion Workflow

1. **Detect instrument type** from file format
2. **Parse native format** (PDF, CSV, Excel)
3. **Map fields** to ASM schema
4. **Validate output** against schema
5. **Export** as ASM JSON or flattened CSV

### Output Options

**ASM JSON:**
- Full semantic structure
- Linked to ontologies
- Machine-readable

**Flattened CSV:**
- Human-readable
- Excel-compatible
- Simpler downstream processing

---

## Tool Connections

| Category | Placeholder | Examples |
|----------|-------------|----------|
| Literature | `~~literature` | PubMed, bioRxiv |
| Clinical Trials | `~~trials` | ClinicalTrials.gov |
| Genomics | `~~genomics` | NCBI, Ensembl |
| Lab Notebook | `~~notebook` | Benchling |
| Data Repository | `~~data` | Synapse, GEO |

### Working Without Connectors

All capabilities work locally:
- Protocol templates standalone
- Nextflow runs on local data
- Single-cell analysis on uploaded files
- Problem selection is conversational

Connectors enhance literature search and data access.
