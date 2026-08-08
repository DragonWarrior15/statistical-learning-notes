## Sequence to Sequence or Encoder Decoder Models
- We need to condition the output on the entire input sequence
- Use encoder architecture to map input to an internal representation
- **Cross attention**: Keys and Values are used from $Z$ (output of encoder), but $Q$ comes from the output sequence
    - This is based on the intuition that the output asks queries which must be answered using the Keys from the input
    - Very similar to user bringing their queries, and the librarian answering based on available Keys with each book
- Training is done using pairs of input and output sentences

Decoder section of this architecture looks as below

```mermaid
graph BT;
    subgraph Left_Column [" "]
        Z[Z];
        KC[K];
        VC[V];
    end

    subgraph Right_Column [" "]
        X --> Kx[K];
        X --> Qx[Q];
        X --> Vx[V];
    end

    AN1[Add and Normalize];
    AN2[Add and Normalize];
    AN3[Add and Normalize];
    MLP[MLP];
    QC[Q];
    A1[Masked Multi-head Self Attention];
    A2[Multi-head Cross Attention];

    X --> AN1;
    Kx --> A1;
    Qx --> A1;
    Vx --> A1;
    A1 --> AN1;

    Z --> KC;
    Z --> VC;
    KC --> A2
    QC --> A2;
    VC --> A2;
    QC --> AN2;
    A2 --> AN2;
    AN1 --> QC;

    AN2 --> MLP;
    MLP --> AN3;
    AN2 --> AN3;
    AN3 --> Y;

    style Left_Column fill:none, stroke:none;
    style Right_Column fill:none, stroke:none;
    style MLP fill:#E0F2FE;
    style AN1 fill:#FEF3C7;
    style AN2 fill:#FEF3C7;
    style AN3 fill:#FEF3C7;
    style A1 fill:#FFEDD5;
    style A2 fill:#FFEDD5;
    style Kx fill: none, stroke: none;
    style Qx fill: none, stroke: none;
    style Vx fill: none, stroke: none;
    style KC fill: none, stroke: none;
    style QC fill: none, stroke: none;
    style VC fill: none, stroke: none;
    style X fill: none, stroke: none;
    style Z fill: none, stroke: none;
    style Y fill: none, stroke: none;

```

This model was originally used in the Attention paper for a translation style task.
