import modal
import numpy as np
from typing import Any
from dataclasses import dataclass

from modalfold import app
from modalfold.base import FoldingAlgorithm
from modalfold.images.esmfold import esmfold_image
from modalfold.utils import MINUTES, MODEL_DIR
from modalfold.images.volumes import model_weights


@dataclass
class ESMFoldOutput:
    frames: np.ndarray
    sidechain_frames: np.ndarray
    unnormalized_angles: np.ndarray
    angles: np.ndarray
    positions: np.ndarray
    states: np.ndarray
    s_s: np.ndarray
    s_z: np.ndarray
    distogram_logits: np.ndarray
    lm_logits: np.ndarray
    aatype: np.ndarray
    atom14_atom_exists: np.ndarray
    residx_atom14_to_atom37: np.ndarray
    residx_atom37_to_atom14: np.ndarray
    atom37_atom_exists: np.ndarray
    residue_index: np.ndarray
    lddt_head: np.ndarray
    plddt: np.ndarray
    ptm_logits: np.ndarray
    ptm: np.ndarray
    aligned_confidence_probs: np.ndarray
    predicted_aligned_error: np.ndarray
    max_predicted_aligned_error: np.ndarray


@app.cls(
    image=esmfold_image,
    gpu="A100-40GB",
    timeout=20 * MINUTES,
    container_idle_timeout=10 * MINUTES,
    volumes={MODEL_DIR: model_weights},
)
class ESMFold(FoldingAlgorithm):
    # We need to properly asses whether using this or the original ESMFold is better
    # based on speed, accuracy, bugs, etc.; as well as customizability
    # For instance, if we want to also allow differently sized structure modules, than this would be good
    @modal.enter()
    def _load(self) -> None:
        from transformers import AutoTokenizer, EsmForProteinFolding

        self.tokenizer = AutoTokenizer.from_pretrained("facebook/esmfold_v1")
        self.model = EsmForProteinFolding.from_pretrained("facebook/esmfold_v1", cache_dir=MODEL_DIR)
        self.device = "cuda"
        self.model = self.model.cuda()
        self.model.eval()
        # TODO: Make chunk size configurable?
        self.model.trunk.set_chunk_size(64)

    @modal.method()
    def fold(self, sequences: list[str]) -> ESMFoldOutput:
        import torch

        # TODO: make sure to the glycine linker thing
        # TODO: check we are doing positional encodings properly
        tokenized = self.tokenizer(sequences, return_tensors="pt", add_special_tokens=False)["input_ids"]
        tokenized = tokenized.to(self.device)
        with torch.inference_mode():
            outputs = self.model(tokenized)
        return self._convert_outputs(outputs)  # TODO: assert the output and validate it

    def _convert_outputs(self, outputs: Any) -> ESMFoldOutput:
        from torch.utils._pytree import tree_map

        outputs = tree_map(lambda x: x.cpu().numpy(), outputs)
        return ESMFoldOutput(**outputs)


# TODO: add an option to return a PDB?
# @staticmethod
# def convert_outputs_to_pdb(outputs):
#     from transformers.models.esm.openfold_utils.protein import to_pdb, Protein as OFProtein
#     from transformers.models.esm.openfold_utils.feats import atom14_to_atom37
#     final_atom_positions = atom14_to_atom37(
#         outputs["positions"][-1], outputs)
#     outputs = {k: v.to("cpu").numpy() for k, v in outputs.items()}
#     final_atom_positions = final_atom_positions.cpu().numpy()
#     final_atom_mask = outputs["atom37_atom_exists"]
#     pdbs = []
#     for i in range(outputs["aatype"].shape[0]):
#         aa = outputs["aatype"][i]
#         pred_pos = final_atom_positions[i]
#         mask = final_atom_mask[i]
#         resid = outputs["residue_index"][i] + 1
#         pred = OFProtein(
#             aatype=aa,
#             atom_positions=pred_pos,
#             atom_mask=mask,
#             residue_index=resid,
#             b_factors=outputs["plddt"][i],
#             chain_index=outputs["chain_index"][i] if "chain_index" in outputs else None,
#         )
#         pdbs.append(to_pdb(pred))
#     return pdbs
