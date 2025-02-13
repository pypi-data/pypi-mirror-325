# Copyright 2023-2024 Luminary Cloud, Inc. All Rights Reserved.
import re
from datetime import datetime
from os import PathLike, path
from typing import Optional, Union

import grpc

from ._client import get_default_client
from ._helpers import (
    create_geometry,
    create_simulation,
    simulation_params_from_json_path,
    timestamp_to_datetime,
    upload_mesh,
    upload_table_as_json,
    upload_c81_as_json,
)
from ._helpers.deprecated import deprecated
from ._proto.api.v0.luminarycloud.geometry import geometry_pb2 as geometrypb
from ._proto.api.v0.luminarycloud.mesh import mesh_pb2 as meshpb
from ._proto.api.v0.luminarycloud.project import project_pb2 as projectpb
from ._proto.api.v0.luminarycloud.simulation import simulation_pb2 as simulationpb
from ._proto.api.v0.luminarycloud.simulation_template import (
    simulation_template_pb2 as simtemplatepb,
)
from ._proto.client import simulation_pb2 as clientpb
from ._wrapper import ProtoWrapper, ProtoWrapperBase
from .enum import GPUType, MeshType, TableType
from .geometry import Geometry
from .mesh import Mesh
from .meshing import MeshAdaptationParams, MeshGenerationParams
from .simulation import Simulation
from .simulation_template import SimulationTemplate
from .tables import RectilinearTable, create_rectilinear_table
from .types import MeshID, ProjectID


@ProtoWrapper(projectpb.Project)
class Project(ProtoWrapperBase):
    """Represents a Project object."""

    id: ProjectID
    name: str
    description: str
    storage_usage_bytes: int

    _proto: projectpb.Project

    @property
    def create_time(self) -> datetime:
        return timestamp_to_datetime(self._proto.create_time)

    @property
    def update_time(self) -> datetime:
        return timestamp_to_datetime(self._proto.update_time)

    def update(
        self,
        *,
        name: str = "",
        description: str = "",
    ) -> None:
        """
        Update/Edit project attributes.

        Mutates self.

        Parameters
        ----------
        name : str, optional
            New project name.
        description : str, optional
            New project description.
        """
        req = projectpb.UpdateProjectRequest(
            id=self.id,
            name=name,
            description=description,
        )
        res = get_default_client().UpdateProject(req)
        self._proto = res.project

    def delete(self) -> None:
        """
        Delete the project.
        """
        req = projectpb.DeleteProjectRequest(
            id=self.id,
        )
        get_default_client().DeleteProject(req)

    def create_geometry(
        self,
        cad_file_path: PathLike,
        *,
        name: Optional[str] = None,
        scaling: Optional[float] = None,
        wait: bool = False,
    ) -> Geometry:
        """
        Create a new geometry in the project by uploading a supported CAD file.

        For more information on supported formats and best practices, see:
        https://docs.luminarycloud.com/en/articles/9274255-upload-cad

        Parameters
        ----------
        cad_file_path : PathLike or str
            Path or URL to the CAD file to upload.

        Other Parameters
        ----------------
        name : str, optional
            Name of the geometry on Luminary Cloud. A default name will be used
            if unset.
        scaling : float, optional
            Scaling to apply to the source CAD file upon import. Defaults to 1.0
            if unset.
        wait : bool, optional
            If set to True, this function will block until the geometry import
            completes. Otherwise, it will return immediately and the import will
            occur in the background. Defaults to False.

        Returns
        -------
        Geometry
            The newly created Geometry.
        """
        _geometry = create_geometry(
            get_default_client(),
            project_id=self.id,
            cad_file_path=cad_file_path,
            name=name,
            scaling=scaling,
            wait=wait,
        )
        return Geometry(_geometry)

    def list_geometries(self) -> list[Geometry]:
        """
        List all geometries in project.

        Returns
        -------
        list[Geometry]
            A list of all available Geometries in the project.
        """
        req = geometrypb.ListGeometriesRequest(project_id=self.id)
        res: geometrypb.ListGeometriesResponse = get_default_client().ListGeometries(req)
        return [Geometry(g) for g in res.geometries]

    def load_geometry_to_setup(self, geometry: Geometry) -> None:
        """
        Load a geometry to the setup phase.
        NOTE: this operation is irreversible and deletes all the existing meshes and simulations
        in the project.

        Parameters
        ----------
        geometry : Geometry
            Geometry to load to the setup phase.
        """
        req = projectpb.LoadGeometryToSetupRequest(
            id=self.id,
            geometry_id=geometry.id,
        )
        get_default_client().LoadGeometryToSetup(req)

    def upload_mesh(
        self,
        path: Union[PathLike, str],
        *,
        name: Optional[str] = None,
        scaling: Optional[float] = None,
        mesh_type: Optional[MeshType] = None,
        do_not_read_zones_openfoam: Optional[bool] = None,
    ) -> Mesh:
        """
        Upload a mesh to the project.

        For more information on supported formats and best practices see:
        https://docs.luminarycloud.com/en/articles/9275233-upload-a-mesh

        Parameters
        ----------
        path : pathlike or str
            Path or URL to the mesh file to upload.

        Other Parameters
        ----------------
        name : str, optional
            Name of the mesh resource on Luminary Cloud. Defaults to the
            filename.
        scaling : float, optional
            If set, apply a scaling factor to the mesh.
        mesh_type : MeshType, optional
            The file format of the mesh file. Required for OpenFOAM format.
        do_not_read_zones_openfoam : bool, default False
            If true, disables reading cell zones in the polyMesh/cellZones file
            for OpenFOAM meshes.
        """
        _mesh = upload_mesh(
            get_default_client(),
            project_id=self.id,
            path=path,
            mesh_type=mesh_type,
            name=name,
            scaling=scaling,
            do_not_read_zones_openfoam=do_not_read_zones_openfoam,
        )
        return Mesh(_mesh)

    @deprecated("Use create_or_get_mesh() instead")
    def create_mesh(
        self,
        params: meshpb.MeshGenerationParams | MeshAdaptationParams | MeshGenerationParams,
        *,
        name: str,
    ) -> Mesh:
        """
        Create a new mesh in the project.

        This method is deprecated. Use create_or_get_mesh() instead.

        Parameters
        ----------
        params : MeshGenerationParams | MeshAdaptationParams
            The parameters to use to create the mesh. If generating a new mesh from an
            existing geometry, use MeshGenerationParams. If adapting a mesh from an existing,
            solution use MeshAdaptationParams.
        name : str
            (Optional) Mesh name. Max 256 characters.
        """

        client = get_default_client()

        req = meshpb.CreateMeshRequest(
            project_id=self.id,
            name=name,
        )

        if isinstance(params, meshpb.MeshGenerationParams):
            req.mesh_generation_params.CopyFrom(params)
        elif isinstance(params, MeshAdaptationParams):
            req.mesh_adaptation_params.CopyFrom(params._to_proto())
        elif isinstance(params, MeshGenerationParams):
            req.mesh_generation_params.CopyFrom(params._to_proto())
            list_geometry_entities_res: geometrypb.ListGeometryEntitiesResponse = (
                client.ListGeometryEntities(
                    geometrypb.ListGeometryEntitiesRequest(geometry_id=params.geometry_id)
                )
            )
            req.mesh_generation_params.volume_params.insert(
                0,
                meshpb.MeshGenerationParams.VolumeParams(
                    min_size=params.min_size,
                    max_size=params.max_size,
                    volumes=[body.lcn_id for body in list_geometry_entities_res.bodies],
                ),
            )
        else:
            raise ValueError("Invalid parameters")

        res: meshpb.CreateMeshResponse = client.CreateMesh(req)
        return Mesh(res.mesh)

    def create_or_get_mesh(
        self,
        params: meshpb.MeshGenerationParams | MeshAdaptationParams | MeshGenerationParams,
        *,
        name: str,
    ) -> Mesh:
        """
        Create a new mesh in the project, or return an existing mesh with the same parameters
        if it already exists.

        Parameters
        ----------
        params : MeshGenerationParams | MeshAdaptationParams
            The parameters to use to create the mesh. If generating a new mesh from an
            existing geometry, use MeshGenerationParams. If adapting a mesh from an existing,
            solution use MeshAdaptationParams.
        name : str
            (Optional) Mesh name. Max 256 characters. Will be ignored if a mesh with the same
            parameters already exists.
        """

        try:
            return self.create_mesh(params, name=name)
        except grpc.RpcError as e:
            if e.code() == grpc.StatusCode.ALREADY_EXISTS:
                message = e.details()
                match = re.search(r"mesh-[a-f0-9-]+$", message)
                if match:
                    existing_mesh_id = match.group(0)
                    req = meshpb.GetMeshRequest(id=existing_mesh_id)
                    res = get_default_client().GetMesh(req)
                    return Mesh(res.mesh)
            raise

    def list_meshes(self) -> list[Mesh]:
        """
        List all meshes in project.
        """
        req = meshpb.ListMeshesRequest(project_id=self.id)
        res = get_default_client().ListMeshes(req)
        return [Mesh(m) for m in res.meshes]

    def create_table(
        self,
        table_type: TableType,
        table_file_path: PathLike,
        simulation_template: SimulationTemplate,
    ) -> RectilinearTable:
        """
        Create a new table in the project and make it available in a simulation template.

        Parameters
        ----------
        table_type : TableType
            The type of table being created, this defines the format expected for the file.
        table_file_path : path-like
            Path to the file (usually a csv or c81 file) with the data used to create the table.
        simulation_template : SimulationTemplate
            Simulation template that is updated with the new table.

        Returns
        -------
        RectilinearTable
            A reference to the created table, which can be used for tabulated simulation parameters.
            For example, profile boundary conditions.
        """
        uploaded_filename = path.basename(table_file_path)
        name = uploaded_filename.rsplit(".", maxsplit=1)[0]
        if table_type == TableType.AIRFOIL_PERFORMANCE:
            url = upload_c81_as_json(get_default_client(), self.id, name, table_file_path)
        else:
            table = create_rectilinear_table(table_type, table_file_path)
            url = upload_table_as_json(get_default_client(), self.id, name, table)
        if not url:
            raise RuntimeError("The table upload failed.")

        # Update the simulation template with the new table reference.
        simulation_template.parameters.table_references[name].url = url
        simulation_template.parameters.table_references[name].table_type = table_type
        simulation_template.parameters.table_references[name].uploaded_filename = uploaded_filename
        simulation_template.update(
            name=simulation_template.name, parameters=simulation_template.parameters
        )

        return RectilinearTable(id=name, name=uploaded_filename, table_type=table_type)

    def create_simulation(
        self,
        mesh_id: MeshID,
        name: str,
        simulation_template_id: str,
        *,
        description: str = "",
        batch_processing: bool = True,
        gpu_type: Optional[GPUType] = None,
        gpu_count: Optional[int] = None,
    ) -> Simulation:
        """
        Create a new simulation.

        Parameters
        ----------
        mesh_id : str
            Mesh ID.
        name : str
            Simulation name. If empty, a default name will be generated.
        simulation_template_id : str
            ID of the SimulationTemplate used to set up the simulation.

        Other Parameters
        ----------------
        description : str, optional
            Simulation description.
        batch_processing : bool, default True
            If True, batch processing will be used for this
            simulation.
            Use Batch Processing on simulations that are not time-sensitive to
            save up to 65% in credits.
        gpu_type : GPUType, optional
            GPU type to use for the simulation.
        gpu_count : int, optional
            Number of GPUs to use for the simulation. Must be specified to a
            positive value if `gpu_type` is specified.
        """
        _simulation = create_simulation(
            get_default_client(),
            self.id,
            mesh_id,
            name,
            simulation_template_id,
            description=description,
            batch_processing=batch_processing,
            gpu_type=gpu_type,
            gpu_count=gpu_count,
        )
        return Simulation(_simulation)

    def list_simulations(self) -> list[Simulation]:
        """
        List all simulations in project.
        """
        req = simulationpb.ListSimulationsRequest(project_id=self.id)
        res = get_default_client().ListSimulations(req)
        return [Simulation(s) for s in res.simulations]

    def list_simulation_templates(self) -> list[SimulationTemplate]:
        """
        List all simulation templates in project.
        """
        req = simtemplatepb.ListSimulationTemplatesRequest(project_id=self.id)
        res = get_default_client().ListSimulationTemplates(req)
        return [SimulationTemplate(s) for s in res.simulation_templates]

    def create_simulation_template(
        self,
        name: str,
        *,
        parameters: Optional[clientpb.SimulationParam] = None,
        params_json_path: Optional[PathLike] = None,
    ) -> SimulationTemplate:
        """
        Create a new simulation template object.

        Parameters
        ----------
        name : str
            Human-readable name to identify the template.
            Does not need to be unique. Max 256 characters.

        Other Parameters
        ----------------
        parameters : SimulationParam, optional
            Complete simulation parameters. Ignored if `params_json_path` is set.
        params_json_path : path-like, optional
            Path to local JSON file containing simulation params.
        """
        if params_json_path is not None:
            parameters = simulation_params_from_json_path(params_json_path)
        elif parameters is None:
            raise Exception("Either parameters or params_json_path must be set")
        req = simtemplatepb.CreateSimulationTemplateRequest(
            project_id=self.id, name=name, parameters=parameters
        )
        res = get_default_client().CreateSimulationTemplate(req)
        return SimulationTemplate(res.simulation_template)


def create_project(
    name: str,
    description: str = "",
) -> Project:
    """
    Create a project owned by the user.

    Parameters
    ----------
    name : str
        Project name.
    description : str
        Project description.
    """
    req = projectpb.CreateProjectRequest(name=name, description=description)
    res = get_default_client().CreateProject(req)
    return Project(res.project)


def get_project(
    id: ProjectID,
) -> Project:
    """
    Get a specific project by ID.

    Parameters
    ----------
    id : str
        Project ID.
    """
    req = projectpb.GetProjectRequest(id=id)
    res = get_default_client().GetProject(req)
    return Project(res.project)


def list_projects() -> list[Project]:
    """
    List projects accessible by the user.
    """
    req = projectpb.ListProjectsRequest()
    res = get_default_client().ListProjects(req)
    return [Project(p) for p in res.projects]
