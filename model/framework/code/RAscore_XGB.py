import os
import pathlib
import numpy as np
import xgboost as xgb

from rdkit import Chem
from rdkit.Chem import AllChem


class RAScorerXGB:
    """
    Prediction of machine learned retrosynthetic accessibility score
    The RAScore is calculated based on the predictions made on 200,000 compounds sampled from ChEMBL.
    The compounds were subjected to retrosynthetic analysis using a CASP tool (AiZynthfinder) and output used as labels to train a binary classifier.

    If the compounds are ChEMBL like use the RAscore models.
    Else if the compounds are more exotic, are small fragments, or closely resemble GDB. GBDscore may give a better result.

    This class facilitates predictions from the resulting model.
    """

    def __init__(self, model_path=None):
        """
        Loads the model.

        :param model_path: path to the XGBoost model (.pkl) file
        :type model_path: pkl
        """
        MODEL= os.path.join(pathlib.Path(os.path.dirname(__file__)).parent.parent, 'checkpoints/XGB_chembl_ecfp_counts/model.json')
        print(MODEL)
        self.xgb_model = xgb.Booster()
        if model_path == None:
            self.xgb_model.load_model(MODEL)
        else:
            self.xgb_model.load_model(model_path)

    def ecfp(self, smiles):
        """
        Converts SMILES into a counted ECFP6 vector with features.

        :param smiles: SMILES representation of the moelcule of interest
        :type smiles: str
        :return: ECFP6 counted vector with features
        :rtype: np.array
        """
        mol = Chem.MolFromSmiles(smiles)
        fp = AllChem.GetMorganFingerprint(mol, 3, useCounts=True, useFeatures=False)
        size = 2048
        arr = np.zeros((size,), np.int32)
        for idx, v in fp.GetNonzeroElements().items():
            nidx = idx % size
            arr[nidx] += int(v)
        return arr

    def predict(self, smiles):
        """
        Predicts score from SMILES.

        :param smiles: SMILES representation of the moelcule of interest
        :type smiles: str
        :return: score
        :rtype: float
        """
        arr = self.ecfp(smiles)
        proba = self.xgb_model.predict(xgb.DMatrix(arr.reshape(1, -1)))
        return proba[0]

